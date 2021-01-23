print('-' * 20, '欢迎光临《唐僧大战白骨精》', '-' * 20)
print('请选择你的身份')
print('\t1.唐僧')
print('\t2.白骨精')
player_choice = input('请选择【1或2】:')
print('-' * 63)
if player_choice == '1':
    print('你将以唐僧的身份进入游戏')
elif player_choice == '2':
    print('不可以选择白骨精，你将以唐僧身份进入游戏')
else:
    print('你输入的内容超出范围，你将以唐僧身份进入游戏')
player_life = 2
player_attack = 2
boss_life = 10
boss_attack = 10
print('-' * 63)
print(f'唐僧，你的血条是{player_life},你的攻击力是{player_attack}')
while True:
    print('-' * 63)
    print('请选择操作')
    print('\t1.练级')
    print('\t2.打BOSS')
    print('\t3.逃跑')
    game_choice = input('请选择【1或2或3】:')
    if game_choice == '1':
        player_life += 2
        player_attack += 2
        print(f'唐僧你升级了，你现在血条是{player_life},你现在的攻击力是{player_attack}')
    elif game_choice == "2":
        print('唐僧攻击了白骨精')
        boss_life -= player_attack
        if boss_life <= 0:
            print(f'白骨精收到了{player_attack}点的攻击，死亡，唐僧胜利')
            break
        else:
            print(f'白骨精受到了{player_attack}点的的攻击')
