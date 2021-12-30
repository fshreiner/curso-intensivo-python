# Podemos usar a palavra reservada in caso seja necessário validar se um valor está numa lista
# Ou usar not, caso seja preciso saber se o valor não está na lista, exemplo:
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')
