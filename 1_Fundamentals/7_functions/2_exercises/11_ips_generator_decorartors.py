# 
def ask_blocks(generate_ip):
    def beforeAction():
        block1 = int(input('Enter the block 1: '))
        block2 = int(input('Enter the block 2: '))
        block3 = int(input('Enter the block 3: '))
        begin = int(input('Enter the begin: '))
        end = int(input('Enter the end:  '))
        return block1, block2, block3, begin, end 
    
    def afterAction(ips):
        for ip in ips:
            print(ip)
    
    def display(*args):
        block1, block2, block3, begin, end = beforeAction()
        ips = generate_ip(block1, block2, block3, begin, end)
        afterAction(ips)
    return display

@ask_blocks
def generate_ip(block1 = 0, block2 = 0, block3 = 0, begin = 0, end = 0 ):
    for ip in range(begin, end):
        yield f'{str(block1)}.{str(block2)}.{str(block3)}.{str(ip)}'

generate_ip()