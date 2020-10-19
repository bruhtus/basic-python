st = {'anu', 'ini'}
print(f'before adding item: {st}')

st.add('itu')
print(f'after adding item: {st}')

st.update({'nganu', 'ngitu', 'ngini'}) #add multiple items using update()
print(f'add multiple items using update(): {st}')
