def m_data(m_name, m_sname, m_age, m_city, m_email,
           m_phone):  # Функция должна принимать параметры как именованные аргументы
    return m_name, m_sname, m_age, m_city, m_email, m_phone


print(
    m_data(m_name="Alex", m_sname="Petrov", m_age=26, m_city="Moscow", m_email="palex@gmail.com", m_phone=87007452644))

# --------------------------version_2-------------------------
print((lambda m_nm, m_sm, m_a, m_c, m_e, m_ph: print(m_nm, m_sm, m_a, m_c, m_e, m_ph))(m_nm="Alan", m_sm="Elen", m_a=32, m_c="ms", m_e = "aemail", m_ph = 4566))
