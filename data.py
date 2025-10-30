import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. 전복 데이터 불러오기
# 'abalone.txt' 파일이 스크립트와 같은 디렉토리에 있다고 가정합니다.
file_path = 'abalone.txt'

# 데이터셋의 컬럼 이름 지정 (파일에 헤더가 없다고 가정)
column_names = ["sex", "length", "diameter", "height", "whole weight", "shucked weight", "viscera weight", "shell weight", "rings"]

# pd.read_csv를 사용하여 파일 불러오기
# 구분자(sep)가 쉼표(,)이고, 헤더가 없으므로 header=None을 지정합니다.
try:
    data = pd.read_csv(file_path, sep=',', header=None, names=column_names)
except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인해주세요: {file_path}")
    exit()

print("### 🐚 원본 전복 데이터 (앞 5개 행) ###")
print(data.head())
print("\n" + "="*50 + "\n")

# 2. 성별 데이터를 label 변수로 따로 저장 및 특성 데이터 분리
label = data['sex']
features = data.drop('sex', axis=1) # 특성 데이터 (수치형)

# 3. Scikit-Learn의 LabelEncoder를 사용한 레이블 인코딩
label_encoder = LabelEncoder()
label_encoded = label_encoder.fit_transform(label)

print("### 🏷️ Label Encoding 결과 확인 (성별 컬럼만) ###")
result_le = pd.DataFrame({
    'Original Sex': label.head(10), 
    'Label Encoded': label_encoded[:10]
})
print(result_le)

print("\n**[매핑된 클래스]**")
# 인코딩된 값에 대응하는 원본 클래스 확인
for i, name in enumerate(label_encoder.classes_):
    print(f"인코딩 값 **{i}**: {name}")

print("\n" + "="*50 + "\n")

# 4. 원-핫 인코딩(One-Hot Encoding) 진행
# Pandas의 get_dummies()를 사용하여 'sex' 컬럼에 원-핫 인코딩 적용
# 이 방법이 일반적으로 범주형 변수를 처리하는 데 선호됩니다.
features_ohe = pd.get_dummies(data, columns=['sex'], prefix='sex')

# 5. 최종적으로 원-핫 인코딩된 결과 확인
print("### 🔥 최종 원-핫 인코딩된 데이터 (앞 5개 행) ###")
print(features_ohe.head())

print("\n**[주요 변경 사항]**")
print(f"* 원본 'sex' 컬럼이 삭제되고, 'sex_F', 'sex_I', 'sex_M' 컬럼이 생성되었습니다.")
