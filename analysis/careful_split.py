import numpy as np

def careful_split(dataframe, columns=['turma', 'lesson', 'student']):
    """
    Constrói dois sub-conjuntos de dados, de modo que não haja repetição da tupla (turma, aula, aluno).
    Ou seja, cada sub-conjunto tem apenas uma informação de relevância, ritmo, satisfação e aprendizagem
    por aula.
    """
    
    df_sorted = dataframe.sort_values(columns)

    def masks(n):
        mask_1 = [False] * n
        mask_2 = [False] * n

        np.random.seed(42)
        idx_1_true = np.random.randint(0, n)
        mask_1[idx_1_true] = True

        if n > 1:
            idx_2_true = np.random.choice(np.argwhere(np.invert(mask_1)).ravel())
            mask_2[idx_2_true] = True
        
        return mask_1, mask_2

    def flatten(list_of_lists):
        return [item for sublist in list_of_lists for item in sublist]

    def check_split(sample):
        assert(sample[columns].value_counts().apply(lambda x: x == 1).all())

    list_of_lists = [masks(n) for n in df_sorted[columns].value_counts().rename('n').reset_index().sort_values(columns).n]
    
    mask_1 = [item[0] for item in list_of_lists]
    mask_2 = [item[1] for item in list_of_lists]
    
    sample_1 = df_sorted[flatten(mask_1)]
    sample_2 = df_sorted[flatten(mask_2)]
    
    check_split(sample_1)
    check_split(sample_2)
    
    return sample_1, sample_2