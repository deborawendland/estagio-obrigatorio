import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(base, name, output_path):

    png_path = '{output_path}\\{name}-frequency.png'.format(output_path=output_path, name=name)

    print ('Saving frequency graph of {name} to {output_path}'.format(output_path=png_path, name=name))

    fig = plt.figure(figsize=(20,8))  
    palette2 = ['#ce2029','#78909c','#ce2029']
    sns.set_style("whitegrid")
    sns.catplot(name, data=base, kind='count', palette='Blues', aspect=3).despine(left=True)
    plt.ylabel("Total cases", fontsize=14)
    plt.xlabel(name, fontsize=14)
    plt.xticks(fontsize=14)
    plt.title('Frequencia de '+name)
    # plt.show() 

    plt.savefig(png_path, bbox_inches="tight")
