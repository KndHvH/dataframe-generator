import string

def get_namelist():
    return ['Ryan', 'Elisa', 'Sara', 'Luís', 'Fernando', 'Alessandra', 'Gabriel', 'Sebastiana', 'Pedro', 'Diego', 'Sônia', 'Tomás', 'Samuel', 'Lucas', 'Carolina', 'Nathan', 'Eduarda', 'Enzo', 'Mário', 'Iago', 'Marcela', 'Josefa', 'Márcia', 'Yago', 'Isabelle', 'Fernanda', 'Daiane', 'Tiago', 'Caio', 'Cláudio', 'Mariana', 'Thiago', 'Flávia', 'Leandro', 'Luiza', 'Rafael', 'Lorenzo', 'Manuel', 'Fátima', 'Calebe', 'Isaac', 'Anthony', 'Alícia', 'Isis', 'Larissa', 'Alexandre', 'Isabel', 'Rebeca', 'Helena', 'Gabrielly', 'Henry', 'Martin', 'Isadora', 'Theo', 'Oliver', 'Hugo', 'Alana', 'Bruna', 'Elza', 'Marcos', 'Betina', 'Bárbara', 'Heloisa', 'Geraldo', 'Clarice', 'Maria', 'Nicole', 'Lúcia', 'Fabiana', 'Kevin', 'Giovanni', 'Laís', 'Emilly', 'Eduardo', 'Liz', 'Renan', 'Raimunda', 'Francisco', 'Daniela', 'Juliana', 'Guilherme', 'Paulo', 'Nelson', 'Raquel', 'Rafaela', 'Débora', 'Gael', 'Cauê', 'Levi', 'Aurora', 'Diogo', 'Teresinha', 'Fábio', 'Ricardo', 'Vitor', 'Bernardo', 'Sophia', 'Otávio', 'Erick', 'Gustavo', 'Eloá', 'Jaqueline', 'Sueli', 'Esther', 'Evelyn', 'Raul', 'Juan', 'Caleb', 'Simone', 'Sarah', 'Rodrigo', 'José', 'Priscila', 'Lucca', 'Murilo', 'Caroline', 'Raimundo', 'Augusto', 'Sandra', 'Pietro', 'Marcelo', 'Pietra', 'Aparecida', 'Carlos', 'Lorena', 'João', 'Valentina', 'Lara', 'Ayla', 'Osvaldo', 'Milena', 'Camila', 'Henrique', 'Giovanna', 'Louise', 'Joaquim', 'Joana', 'Miguel', 'Sophie', 'Mariane', 'Marina', 'Kamilly', 'Benjamin', 'Olivia', 'Benício', 'Leonardo', 'Aline', 'Breno', 'Bento', 'Danilo', 'Emanuel', 'Ian', 'Maya', 'Heitor', 'Gabriela', 'Beatriz', 'Isabelly', 'Noah', 'Marli', 'Nicolas', 'Jorge', 'Jéssica', 'Manuela', 'Felipe', 'Cauã', 'Rosa', 'Analu', 'Andreia', 'Filipe', 'Jennifer', 'Elias', 'Isabela', 'Tânia', 'Rita', 'Luan', 'Thales', 'Davi', 'Vera', 'Bryan', 'Igor', 'Sérgio', 'Ruan', 'Malu', 'Letícia', 'Kauê', 'Victor', 'Rosângela', 'Sabrina', 'Vanessa', 'Antonella', 'Eliane', 'Márcio', 'Manoel', 'Catarina', 'Antônia', 'Bruno', 'Adriana', 'Amanda', 'Alice', 'Melissa', 'Sebastião']

def get_lastnamelist():
    return ['Francisca', 'Alessandra', 'Nina', 'Maitê', 'Martins', 'Teixeira', 'Luzia', 'Carvalho', 'Carolina', 'Luz', 'Assunção', 'Marcela', 'Josefa', 'Allana', 'Viana', 'Fernandes', 'Isabelle', 'Caldeira', 'Mata', 'Fernanda', 'Daiane', 'Lívia', 'Campos', 'Cunha', 'Pinto', 'Flávia', 'Oliveira', 'Luiza', 'Rodrigues', 'Moura', 'Pires', 'Lima', 'Duarte', 'Isis', 'Conceição', 'Santos', 'Bernardes', 'Rebeca', 'Helena', 'Almada', 'Laura', 'Real', 'Isadora', 'Farias', 'Nascimento', 'Alana', 'Heloise', 'Bruna', 'Cardoso', 'Betina', 'Elza', 'Clarice', 'Castro', 'Silveira', 'Paula', 'Nicole', 'Lúcia', 'Emilly', 'Laís', 'Fabiana', 'Liz', 'Novaes', 'Giovana', 'Aurora', 'Teresinha', 'Peixoto', 'Aparício', 'Sophia', 'Paz', 'Rezende', 'Jaqueline', 'Aragão', 'Cristiane', 'Esther', 'Lavínia', 'Isabella', 'Assis', 'Simone', 'Sarah', 'Emanuelly', 'Caroline', 'Brenda', 'Sandra', 'Andrea', 'Carla', 'Mendes', 'Aparecida', 'Barbosa', 'Lorena', 'Tereza', 'Freitas', 'Camila', 'Louise', 'Nogueira', 'Sophie', 'Marina', 'Mariane', 'Kamilly', 'Olivia', 'Ribeiro', 'Silva', 'Aline', 'Gomes', 'Baptista', 'Gonçalves', 'Luna', 'Mota', 'Regina', 'Souza', 'Galvão', 'Ferreira', 'Beatriz', 'Moraes', 'Gabriela', 'Marli', 'Nair', 'Figueiredo', 'Manuela', 'Monteiro', 'Agatha', 'Natália', 'Rosa', 'Vieira', 'Cavalcanti', 'Andreia', 'Jennifer', 'Rayssa', 'Sales', 'Isabela', 'Stefany', 'Tânia', 'Dias', 'Rita', 'Vera', 'Julia', 'Lopes', 'Malu', 'Letícia', 'Costa', 'Jesus', 'Rosângela', 'Rocha', 'Sabrina', 'Luciana', 'Cruz', 'Vanessa', 'Antonella', 'Ana', 'Nunes', 'Catarina', 'Antônia', 'Melissa', 'Neves']


def get_letters_list():
    letters = string.ascii_uppercase
    final = list(letters)

    for v in letters:
        for i in range(len(letters)):
            final.append(f'{v}{string.ascii_uppercase[i]}')

    return final
