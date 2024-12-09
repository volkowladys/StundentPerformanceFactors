import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Заголовок додатка
st.title("Аналіз результатів студентів")
st.write("Цей застосунок створено для візуалізації різних аспектів студентських даних.")

# Завантаження даних автоматично
@st.cache_data
def load_data():
    # Завантаження файлу із вказаного шляху
    return pd.read_csv('data/student_performance.csv')

# Завантаження даних
data = load_data()


# Вибір візуалізації
option = st.selectbox(
    "Виберіть візуалізацію:",
    [
        "Розподіл результатів іспитів",
        "Розподіл кількості годин навчання",
        "Розподіл рівнів мотивації",
        "Участь у позакласних заходах",
        "Розподіл рівнів доходу сімей",
        "Зв'язок годин навчання і результатів іспитів",
        "Вплив позакласних заходів і труднощів",
        "Освіта батьків, дохід сім'ї та результати",
        "Вплив годин сну на результати",
        "Вплив фізичної активності на результати",
    ],
)

# Візуалізації
if option == "Розподіл результатів іспитів":
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Exam_Score'], kde=True, bins=20, color='blue')
    plt.title("Розподіл результатів іспитів")
    plt.xlabel("Результат іспиту")
    plt.ylabel("Кількість студентів")
    st.pyplot(plt)

elif option == "Розподіл кількості годин навчання":
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Hours_Studied'], kde=True, bins=20, color='green')
    plt.title("Розподіл кількості годин навчання")
    plt.xlabel("Години навчання")
    plt.ylabel("Кількість студентів")
    st.pyplot(plt)

elif option == "Розподіл рівнів мотивації":
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Motivation_Level', palette='viridis')
    plt.title("Розподіл рівнів мотивації")
    plt.xlabel("Рівень мотивації")
    plt.ylabel("Кількість студентів")
    st.pyplot(plt)

elif option == "Участь у позакласних заходах":
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Extracurricular_Activities', palette='coolwarm')
    plt.title("Участь у позакласних заходах")
    plt.xlabel("Позакласні заходи")
    plt.ylabel("Кількість студентів")
    st.pyplot(plt)

elif option == "Розподіл рівнів доходу сімей":
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Family_Income', palette='pastel')
    plt.title("Розподіл рівнів доходу сімей")
    plt.xlabel("Дохід сім'ї")
    plt.ylabel("Кількість студентів")
    st.pyplot(plt)

elif option == "Зв'язок годин навчання і результатів іспитів":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Hours_Studied', y='Exam_Score', hue='Motivation_Level', palette='viridis')
    plt.title("Зв'язок між годинами навчання, мотивацією та успішністю")
    plt.xlabel("Години навчання")
    plt.ylabel("Результат іспиту")
    plt.legend(title="Рівень мотивації")
    st.pyplot(plt)

elif option == "Вплив позакласних заходів і труднощів":
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='Extracurricular_Activities', y='Exam_Score', hue='Learning_Disabilities', palette='coolwarm')
    plt.title("Вплив позакласних заходів та труднощів на результати")
    plt.xlabel("Позакласні заходи")
    plt.ylabel("Результат іспиту")
    plt.legend(title="Навчальні труднощі")
    st.pyplot(plt)

elif option == "Освіта батьків, дохід сім'ї та результати":
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x='Parental_Education_Level', y='Exam_Score', hue='Family_Income', palette='pastel')
    plt.title("Освіта батьків, дохід сім'ї та результати")
    plt.xlabel("Рівень освіти батьків")
    plt.ylabel("Результат іспиту")
    st.pyplot(plt)

elif option == "Вплив годин сну на результати":
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Sleep_Hours', y='Exam_Score', marker='o', ci=None, color='blue')
    plt.title("Вплив годин сну на результати")
    plt.xlabel("Години сну")
    plt.ylabel("Результат іспиту")
    st.pyplot(plt)

elif option == "Вплив фізичної активності на результати":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Physical_Activity', y='Exam_Score', hue='Parental_Education_Level', palette='muted')
    plt.title("Вплив фізичної активності на результати")
    plt.xlabel("Фізична активність")
    plt.ylabel("Результат іспиту")
    plt.legend(title="Освіта батьків")
    st.pyplot(plt)
