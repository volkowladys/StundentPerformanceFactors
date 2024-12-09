# Фактори успішності студентів
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://student-performance-factors.streamlit.app/)

## Мета

- Проаналізувати вплив різних факторів на академічну успішність студентів (підсумковий результат іспиту) та виявити ключові фактори, що впливають на їх оцінку.

## Основні питання

- Як навчальні навички (кількість годин на навчання, мотивація) впливають на підсумкові результати іспитів?
- Як зовнішні чинники, такі як участь у позакласних заходах, фізична активність та наявність труднощів у навчанні впливають на результати іспитів?
- Як соціоекономічні чинники (дохід сім'ї, рівень освіти батьків) пов'язані з академічною успішністю?

## Дані

Проект містить в собі різні фактори, що впливають на успішність студентів у навчанні, а саме:

- Години вивчення - Кількість годин, що витрачаються на навчання на тиждень.
- Відвідуваність – відсоток відвідуваних занять.
- Батьківська участь - Рівень участі батьків в освіті учня (низький, середній, високий).
- Доступ к ресурсам – Доступність освітніх ресурсів (низька, середня, висока).
- Позакласні заходи – Участь у позакласних заходах (Так, Ні).
- Години сну – Середня кількість годин сну за ніч.
- Результати попередніх іспитів.
- Рівень мотивації – рівень мотивації студента (низький, середній, високий).
- Доступ до Інтернету – доступ до Інтернету (Так, Ні).
- Репетиторство – Кількість відвіданих занять із репетитором на місяць.
- Сімейний дохід - Рівень доходу сім'ї (низький, середній, високий).
- Якість викладачів – Якість навчального процесу у викладачів (низька, середня, висока).
- Тип школи - Тип школи (державна, приватна).
- Вплив однолітків - Вплив однолітків на успішність (позитивний, нейтральний, негативний).
- Фізична активність - Середня кількість годин фізичної активності на тиждень.
- Проблеми навчання – Наявність труднощів у навчанні (Так, Ні).
- Рівень батьківської освіти – Рівень освіти батьків (середня школа, коледж, аспірантура).
- Відстань від будинку - Відстань від будинку до школи (близько, середньо, далеко).
- Стать – Стать студента (чоловік, жінка).
- Оцінка іспиту – Підсумковий результат іспиту.

## Методологія

1. Збір даних:
- Джерело даних: Набір даних про фактори, що впливають на успішність студентів.
- Обсяг даних: Дані включають різні параметри, такі як кількість годин навчання, відвідуваність, рівень мотивації, участь у позакласних заходах, а також соціоекономічні характеристики.

2. Обробка даних:
- Попереднє очищення даних: Перевірка на пропуски даних та їх обробка
- Підготовка даних для подальшого аналізу

3. Аналіз:
- Визначення взаємозв'язків між кількістю годин на навчання, мотивацією та підсумковими результатами іспитів.
- Аналіз кореляцій між соціоекономічними факторами та успішністю (наприклад, дохід сім'ї, рівень освіти батьків).
- Аналіз чинників, такі як участь у позакласних заходах, фізична активність та наявність труднощів у навчанні впливають на результати іспитів?
- Оцінка важливості кожного фактора (наприклад, мотивація, відвідуваність, батьківська участь) у прогнозі оцінок.
- Поділ даних на групи (наприклад, на основі рівня доходу або типу школи) для аналізу відмінностей у успішності студентів.

4. Візуалізація:
- Використання лінійних графіків для відображення залежності між навчальними, зовнішними,соціоекономічними факторами та підсумковими балами.
- Візуалізація груп студентів з урахуванням подібності характеристик (наприклад, мотивація, доступом до ресурсів).

## Джерела

[Kaggle / Student Performance Factors](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors/data)

## Інструменти та бібліотеки

Буде використовувати різні бібліотеки Python для аналізу даних, зокрема:
- Pandas
- matplotlib
- streamlit
- seaborn
- matplotlib.pyplot

## Очікувані результати

- В результаті аналізу можна виділити ключові фактори, які мають найбільший вплив на академічну успішність.
- Можуть бути надані рекомендації для покращення показників успішності, такі як збільшення годин навчання, покращення доступу до ресурсів, підтримка батьків, збільшення кількості сну та фізичної активності.
- Якщо аналіз підтверджує ці припущення, це може допомогти школам та батькам зосередитись на найважливіших аспектах для покращення академічних результатів студентів.

## Висновки

- Основні фактори: Аналіз виявить ключові змінні, які мають найбільший вплив на успішність студентів. Наприклад, такі фактори, як мотивація, кількість годин навчання, доступ до освітніх ресурсів можуть бути сильними провісниками підсумкових оцінок.
- Вплив зовнішніх умов: Можливо, буде виявлено, що такі фактори, як участь у позакласних заходах, фізична активність або наявність труднощів у навчанні також відіграють роль у успішності.
- Соціоекономічні відмінності: Дослідження покаже, як сімейний дохід та рівень освіти батьків впливають на результати іспитів, а також які типи шкіл забезпечують вищі результати.
- Рекомендації: На основі аналізу можна буде запропонувати рекомендації для покращення академічної успішності, такі як збільшення батьківської участі, покращення доступності освітніх ресурсів або проведення додаткових занять (репетиторства) для покращення результатів іспитів.

---
## Jupyter Notebook
https://www.datacamp.com/datalab/w/ee984919-45bc-424a-860e-27f3c34cb19a
