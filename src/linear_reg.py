import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 재사용을 위해 랜덤값을 초기화 합니다.
torch.manual_seed(42)

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[3], [6], [9]])

W = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
hypothesis = x_train * W + b

cost = torch.mean((hypothesis - y_train) ** 2)
optimizer = optim.SGD([W, b], lr=0.01)

nb_epochs = 1000  # 원하는만큼 경사 하강법을 반복
for epoch in range(nb_epochs + 1):
    hypothesis = x_train * W + b
    cost = torch.mean((hypothesis - y_train) ** 2)
    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print(
            "Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}".format(
                epoch, nb_epochs, W.item(), b.item(), cost.item()
            )
        )

test_var = torch.FloatTensor([[4.0]])
# 입력한 값 4에 대해서 예측값 y를 계산해서 pred_y에 저장
with torch.no_grad():
    pred_y = test_var * W + b
    print("훈련 후 입력이 4일 때의 예측값 :", pred_y)

# nn.Module 로 구현하는 선형회귀
import torch
import torch.optim as optim

# 재사용을 위해 랜덤값을 초기화 합니다.
torch.manual_seed(42)


class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


model = LinearRegressionModel()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

nb_epochs = 1000
for epoch in range(nb_epochs + 1):
    prediction = model(x_train)
    cost = F.mse_loss(
        prediction, y_train
    )  # <== 파이토치에서 제공하는 평균 제곱 오차 함수
    optimizer.zero_grad()
    cost.backward()  # backward 연산
    optimizer.step()

    if epoch % 100 == 0:
        print("Epoch {:4d}/{} Cost: {:.6f}".format(epoch, nb_epochs, cost.item()))

new_var = torch.FloatTensor([[4.0]])
# 입력한 값 4에 대해서 예측값 y를 리턴받아서 pred_y에 저장
with torch.no_grad():
    pred_y = model(new_var)  # forward 연산
    print("훈련 후 입력이 4일 때의 예측값 :", pred_y)
