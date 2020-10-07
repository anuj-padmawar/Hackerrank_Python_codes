import re

for i in range(int(input())):
    x=''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}',x)
        assert re.search(r'\d\d\d',x)
        assert not re.search(r'[^a-zA-Z0-9]',x)
        assert not re.search(r'(.)\1',x)
        assert len(x)==10
    except:
        print('Invalid')
    else:
        print('Valid')

