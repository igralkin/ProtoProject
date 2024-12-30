#!/bin/bash

# Проверка User Service
echo "Testing User Service: Login"
grpcurl -plaintext -d '{"username": "test", "password": "1234"}' localhost:50051 user.UserService/Login

# Проверка Order Service
echo "Testing Order Service: CreateOrder"
grpcurl -plaintext -d '{"user_id": "123", "product_id": "p1", "quantity": 2}' localhost:50052 order.OrderService/CreateOrder

echo "Testing Order Service: GetOrderStatus"
grpcurl -plaintext -d '{"order_id": "order-123"}' localhost:50052 order.OrderService/GetOrderStatus

echo "Testing Payment Service: ProcessPayment"
grpcurl -plaintext -d '{"order_id": "order-123", "amount": 100.50}' localhost:50053 payment.PaymentService/ProcessPayment
grpcurl -plaintext -d '{"order_id": "order-123", "amount": -10}' localhost:50053 payment.PaymentService/ProcessPayment