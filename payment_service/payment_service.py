from concurrent import futures
import grpc
import payment_service_pb2
import payment_service_pb2_grpc
from grpc_reflection.v1alpha import reflection

class PaymentService(payment_service_pb2_grpc.PaymentServiceServicer):
    def ProcessPayment(self, request, context):
        if request.amount <= 0:
            return payment_service_pb2.PaymentResponse(
                payment_id="",
                status="FAILED",
                message="Invalid amount"
            )
        return payment_service_pb2.PaymentResponse(
            payment_id="payment-123",
            status="SUCCESS",
            message="Payment processed successfully"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_service_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)

    # Enable reflection
    SERVICE_NAMES = (
        payment_service_pb2.DESCRIPTOR.services_by_name['PaymentService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
