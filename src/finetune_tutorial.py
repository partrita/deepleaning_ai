from datasets import load_dataset
from transformers import TrainingArguments, Trainer
import numpy as np
import evaluate
from transformers import AutoModelForSequenceClassification

# 파인튜닝할 데이터셋 준비
dataset = load_dataset("yelp_review_full")
# dataset["train"][100]

from transformers import AutoTokenizer

# 텍스트를 처리하고 서로 다른 길이의 시퀀스 패딩 및 잘라내기 전략을 포함하려면 토크나이저가 필요
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


# map 메서드를 사용하여 전체 데이터셋에 전처리 함수를 적용
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# 데이터셋의 작은 부분 집합을 만들어 미세 튜닝 작업 시간을 줄이기
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))


# 모델 가져오기
model = AutoModelForSequenceClassification.from_pretrained(
    "google-bert/bert-base-cased", num_labels=5
)




# 평가하기
metric = evaluate.load("accuracy")


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)




# 체크포인트(checkpoints)를 저장할 위치를 지정합니다
training_args = TrainingArguments(output_dir="test_trainer")

# 훈련하기
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()
