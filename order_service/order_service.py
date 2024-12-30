from concurrent import futures
import grpc
import order_service_pb2
import order_service_pb2_grpc
import user_service_pb2
import user_service_pb2_grpc
from grpc_reflection.v1alpha import reflection


class OrderService(order_service_pb2_grpc.OrderServiceServicer):
    def __init__(self):
        # Настраиваем клиент для User Service
        self.user_service_channel = grpc.insecure_channel('user_service:50051')
        self.user_service_stub = user_service_pb2_grpc.UserServiceStub(self.user_service_channel)

    def CreateOrder(self, request, context):
        # Проверяем существование пользователя
        try:
            user_response = self.user_service_stub.GetUser(user_service_pb2.GetUserRequest(user_id=request.user_id))
            if not user_response.user_id:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("User not found")
                return order_service_pb2.OrderResponse()
        except grpc.RpcError as e:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details("User Service unavailable")
            return order_service_pb2.OrderResponse()

        # Создаем заказ, если пользователь найден
        return order_service_pb2.OrderResponse(
            order_id="order-123",
            status="Order Created"
        )

    def GetOrderStatus(self, request, context):
        return order_service_pb2.OrderStatusResponse(
            order_id=request.order_id,
            status="In Progress"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_service_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)

    SERVICE_NAMES = (
        order_service_pb2.DESCRIPTOR.services_by_name['OrderService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
