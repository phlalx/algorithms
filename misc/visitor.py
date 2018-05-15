class Exp:

  def eval(self, env):
    assert False

  def accept(self, visitor):
    assert False

class Int(Exp):

  def __init__(self, v):
    self.v = v

  def eval(self, env):
    return self.v

  def accept(self, visitor):
    return visitor.visit_int(self)

class Add(Exp):

  def __init__(self, e1, e2):
    self.e1 = e1
    self.e2 = e2

  def eval(self, env):
    return self.e1.eval(env) + self.e2.eval(env)

  def accept(self, visitor):
    return visitor.visit_add(self)

class Var(Exp):

  def __init__(self, v):
    self.v = v

  def eval(self, env):
    return env[self.v]

  def accept(self, visitor):
    return visitor.visit_var(self)

class EvalVisitor:

  def __init__(self, env):
    self.env = env

  def visit_int(self, exp):
    return exp.v 

  def visit_var(self, exp):
    return self.env[exp.v]

  def visit_add(self, exp):
    return exp.e1.accept(self) + exp.e2.accept(self)

class PrintVisitor():

  def visit_int(self, exp):
    return str(exp.v)

  def visit_var(self, exp):
    return str(exp.v)

  def visit_add(self, exp):
    return "+(" + exp.e1.accept(self) + "," + exp.e2.accept(self) + ")"

def test1():
  e = Add(Int(1), Add(Int(2), Var('x')))
  env = { 'x': 42 }
  print (e.eval(env))
  print (e.accept(EvalVisitor(env)))

def gen_name():
    for x in "abcdefghijklmnopqrstuvwxyz":
      yield x

    i = 0
    while True:
        yield 'node_' + str(i)
        i = i + 1

gen_name = gen_name()

class AlphaConvertVisitor:

  def __init__(self, env):
    self.env = env

  def visit_int(self, exp):
    return exp

  def visit_var(self, exp):
    if exp.v in self.env:
      return Var(self.env[exp.v])
    else:
      new_var = next(gen_name)
      self.env[exp.v] = new_var
      return Var(new_var)

  def visit_add(self, exp):
    return Add(exp.e1.accept(self), exp.e2.accept(self))

def test2():
  acv = AlphaConvertVisitor({})
  e = Add(Var('x'), Add(Var('y'), Var('x')))
  e2 = e.accept(acv)  
  print(e2.accept(PrintVisitor()))

test1()
test2()


