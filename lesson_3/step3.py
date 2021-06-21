def smm(num1, num2, num3):
    m_list = [num1, num2, num3]
    m_list.remove(min(m_list))
    return sum(m_list)

print(smm(4, 7, 6))
