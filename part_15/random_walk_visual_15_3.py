# -*- coding: cp936 -*-
# ��ϸ��P297
# �������,���ӻ�
# ����·��ͼ,ģ������˶�

import matplotlib.pyplot as plt
from random_walk import RandomWalk



# ֻҪ�����ڻ״̬���Ͳ��ϵ�ģ���������

while True:
    # ����һ��RandomWalk��ʵ��
    rw = RandomWalk(300)
    rw.fill_walk()
    
    # ���û�ͼ���ڵĳߴ�
    plt.figure(figsize=(10, 6))
    
    # ����·��ͼ
    plt.plot(rw.x_values, rw.y_values, ls='-.', linewidth=1, c='b', marker='+')
    
    # ͻ�������յ�
    plt.scatter(0,0, c='red', edgecolor='none', s=300)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', 
            edgecolor='none', s=300)
            
    # ����������
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    
    # ����һ���������
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running == 'N':
        break


            
