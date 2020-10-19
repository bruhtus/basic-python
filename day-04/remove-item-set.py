st = {'anu', 'ini', 'itu'}
print(f'before removing item: {st}')

st.remove('ini')
print(f'after removing item: {st}')

st.add('ini')
print(f'after adding item: {st}')

st.pop()
print(f'after remove the last item: {st}')
