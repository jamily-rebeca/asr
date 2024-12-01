import json
from datetime import datetime

class Horario:
    def __init__(self, idHorario, horario):
        self.set_idHorario(idHorario)
        self.set_horario(horario)
        self.set_confirmado(False)
        self.set_idCliente(0)
        self.set_idServico(0)

    def set_idHorario(self, idHorario: int):
        self.__idHorario = idHorario

    def get_idHorario(self):
        return self.__idHorario
    
    def set_horario(self, horario):
        if horario:
            self.__horario = horario
        else:
            raise ValueError("determine um horário")

    def get_horario_str(self):
    #     strHorario = datetime.strftime(self.__horario, "%d/%m/%Y")
    #     return strHorario
        return self.__horario
    
    def get_horario(self):
        return self.__horario

    def set_confirmado(self, confirmado):
      self.__confirmado = confirmado

    def get_confirmado(self):
      return self.__confirmado

    def set_idCliente(self, id_cliente):
      self.__idCliente = id_cliente

    def get_idCliente(self):
      return self.__idCliente

    def set_idServico(self, id_servico):
       self.__idServico = id_servico

    def get_idServico(self):
      return self.__idServico


    def __str__(self):
        return f"{self.get_idHorario()} - {self.get_horario_str()}"
    
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["data"] = self.data.strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.confirmado
      dic["id_cliente"] = self.id_cliente
      dic["id_servico"] = self.id_servico
      return dic    

class Horarios:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.data = obj.data
      c.confirmado = obj.confirmado
      c.id_cliente = obj.id_cliente
      c.id_servico = obj.id_servico
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def salvar(cls):
    horario = []
    for h in cls.objetos:
       horario.append(
          {
            "id": h.get_idHorario(),
            "data": h.get_horario_str(),
            "confirmado": h.get_confirmado(),
            "id_cliente": h.get_idCliente(),
            "id_servico": h.get_idServico(),
          }
       )

    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)


  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(
             obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.confirmado = obj["confirmado"]
          c.id_cliente = obj["id_cliente"]
          c.id_servico = obj["id_servico"]
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



