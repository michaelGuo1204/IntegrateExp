# -*- coding: utf-8 -*
import matplotlib.pyplot as plt
import numpy as np




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total={'Exp#2': {'OD240':[0.348,1.075,1.740,1.287,2.104,2.210,2.301,2.451,2.295],'pH':[3.9,3.9,3.4,3.2,3.1,3,3,3,3],'Alko':[3.5,6,10,14,16.5,19,19,22,22],'Brix':[27.2,24.3,23,19.3,17.2,15.7,14,12,11.8],'Result':[5,4,2,4]},
           'Exp#1':{'OD240':[0.452,1.278,1.924,1.824,2.341,2.056,2.097,2.265,2.490],'pH':[3.9,3.9,3.2,3.1,3.0,2.8,2.7,2.6,2.5],'Alko':[3,6,10,13.5,16,16.5,16,18,18],'Brix':[22.7,20.2,16.4,12.3,9.5,9,9,7,7],'Result':[4,3,5,4]},
           'Control':{'OD240':[0.643,1.683,2.021,2.702,2.502,2.436],'pH':[3.9,3.9,3.1,2.8,2.6,2.5],'Alko':[3,5,8,10,11,10],'Brix':[14.1,11.2,6.8,6.0,5.1,5.1],'Result':[3,2,1,3]}
           }
    fig_control=plt.figure()
    ax_control=fig_control.add_subplot(projection='3d')
    colors = ['r', 'g', 'b']
    keys = ['OD240', 'pH', 'Alko', 'Brix','Result']
    yticks=[3,2,1]
    for key in keys:
        fig_control = plt.figure()
        ax_control = fig_control.add_subplot(projection='3d')
        for data, color, trick in zip(total.items(), colors, yticks):
            x = list(range(data[1][key].__len__()))
            y=data[1][key]
            ax_control.bar(x, y, zs=trick, zdir='y', color=color,alpha=0.3)
            ax_control.set_xlabel('Days')
            ax_control.set_ylabel('Case')
            ax_control.set_zlabel(key)
            ax_control.set_yticks(yticks)
        plt.title('{} Bar'.format(key))
        plt.savefig('{} Bar.svg'.format(key),dpi=500)
    label=np.array(['Color','Aroma','Style','Quan'])
    angles = np.linspace(0, 2 * np.pi, len(label), endpoint=False)
    #angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    stats=total['Control']['Result']
    #stats = np.concatenate((stats, [stats[0]]))
    ax.plot(angles, stats, 'o-', linewidth=0)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, label)
    plt.title('The result of Cotrol')
    plt.savefig('The result of Cotrol.svg')
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    stats = total['Exp#1']['Result']
    # stats = np.concatenate((stats, [stats[0]]))
    ax.plot(angles, stats, 'o-', linewidth=0)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, label)
    plt.title('The result of Exp#1')
    plt.savefig('The result of Exp#1.svg',dpi=500)
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    stats = total['Exp#2']['Result']
    # stats = np.concatenate((stats, [stats[0]]))
    ax.plot(angles, stats, 'o-', linewidth=0)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, label)
    plt.title('The result of Exp#2')
    plt.savefig('The result of Exp#2.svg',dpi=500)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
