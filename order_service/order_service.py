from concurrent import futures
import grpc
import order_service_pb2
import order_service_pb2_grpc

class OrderService(order_service_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
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
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
