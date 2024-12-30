from concurrent import futures
import grpc
import user_service_pb2
import user_service_pb2_grpc
from grpc_reflection.v1alpha import reflection


class UserService(user_service_pb2_grpc.UserServiceServicer):
    def Login(self, request, context):
        return user_service_pb2.LoginResponse(
            user_id="123",
            token="mock-token",
            message="Login successful"
        )

    def GetUser(self, request, context):
        return user_service_pb2.UserResponse(
            user_id=request.user_id,
            username="test_user",
            email="test_user@example.com"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    SERVICE_NAMES = (
        user_service_pb2.DESCRIPTOR.services_by_name['UserService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
