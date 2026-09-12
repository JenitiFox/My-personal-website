import streamlit as st

st.set_page_config(page_title = "Мій Супер-додаток", layout="wide")

st.title("Ласкаво прошу до мого додатку! 🎶")

tab1, tab2 = st.tabs(["Про мене", "Мій інструмент"])
with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/275309020?v=4", width=200)
    with col2:
        st.subheader("Привіт, я майбутній Python Developer!")
        st.write("Я навчаюся в Малій Комп'ютерній Академії ItStep. Створюю круті веб-додатки та вивчаю штучний інтелект")

        with st.container():
            st.info("Контакти для зв'язку")
            st.markdown("GitHub: https://github.com/JenitiFox")
            st.markdown("Email: genyakov15@gmail.com")
with tab2:
    st.header("Корисний інструмент: Конвертор температури")
    st.write("Цей інструмент допоможе швидко перевести градуси Цельсій у Фаренгейт")
    с1, с2 = st.columns(2)
    c1 = number = st.number_input("Введіть значення Цельсію:", value = 0.0)
    result = number * 1.8 + 32
    c2 = st.info(f"Результат конвертації: {result}")
# st.write("Все, що не робиться — робиться для чогось")

# user_name = st.text_input("Як тебе звати?")

# if st.button("Привітатися"):
#     if user_name:
#         st.success(f"Привіт, {user_name}! Радий бачити тебе на моєму сайті!")
#     else:
#         st.warning("Будь ласка, введи своє ім'я")

# st.subheader("Завантаж своє фото")
# uploaded_file = st.file_uploader("Оберіть зображення...", type=["jpg","jped","png"])

# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Твоє завантажене фото", use_container_width=True)

# st.title("Всякому місту — звичай і права " \
# "Григорій Сковорода")

# st.write("")

# st.write("Всякому місту — звичай і права")
# st.write("Всяка тримає свій ум голова")
# st.write("Всякому серцю — любов і тепло")
# st.write("Всякеє горло свій смак віднайшло")

# st.write("")

# st.write("Я ж у полоні нав'язливих дум")
# st.write("Лише одне непокоїть мій ум")

# st.write("")

# st.write("Панські Петро для ченців тре кутки")
# st.write("Федір-купець обдурити прудкий")
# st.write("Той зводить дім свій на модний манір")
# st.write("Інший гендлює, візьми перевір")

# st.write("")

# st.write("Я ж у полоні нав'язливих дум")
# st.write("Лише одне непокоїть мій ум")

# st.write("")

# st.write("Той безперевно стягає поля")
# st.write("Сей іноземних заводить телят")
# st.write("Ті на ловецтво готують собак")
# st.write("В сих дім, як вулик, гуде від гуляк")

# st.write("")

# st.write("Я ж у полоні нав'язливих дум")
# st.write("Лише одне непокоїть мій ум")

# st.write("")

# st.write("Ладить юриста на смак свій права")
# st.write("З диспутів в учня тріщить голова")
# st.write("Тих непокоїть венерин Амур —")
# st.write("Всякому голову крутить свій дур")

# st.write("")

# st.write("В мене ж турботи тільки одні")
# st.write("Як з ясним розумом вмерти мені")

# st.write("")

# st.write("Знаю, що смерть, як коса замашна")
# st.write("Навіть царя не обійде вона")
# st.write("Байдуже смерті, мужик то чи цар —")
# st.write("Все пожере як солома пожар")

# st.write("")
# st.write("")

# st.write("Хто ж бо зневажить страшну її сталь...?")
# st.write("Той, в кого совість як чистий кришталь")