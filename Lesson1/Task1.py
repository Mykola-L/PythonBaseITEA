quantitiProduct = input('Введіть, будь-ласка, кількість копій товару ')
priceProduct = input('Введіть, будь-ласка, ціну за одиницю товару ')
quantitiProduct = int(quantitiProduct)
priceProduct = int(priceProduct)
costProduct = priceProduct * quantitiProduct
print('Загальна вартість продуктів', costProduct, 'гривень')
