class Program:
    def __init__(self, function_defs):
        self.function_defs = function_defs


class FunctionDef:  # signature, “(”, parameters, “)”, “{“, block, “}” ;
    def __init__(self, signature, parameters, block):
        self.signature = signature
        self.parameters = parameters
        self.block = block

    def accept(self, visitor):
        return visitor.visit_function_def(self)


class FunctionCall:  # id, “(“, arguments, “)”;
    def __init__(self, _id, arguments):
        self.id = _id
        self.arguments = arguments

    def accept(self, visitor):
        visitor.visit_function_call(self)


class Signature:  # type, id ;
    def __init__(self, _type, _id):
        self.type = _type
        self.id = _id


class Parameters:  # [ signature, { “,”, signature } ];
    def __init__(self, signatures):
        self.signatures = signatures


class Arguments:  # [ expression { “,”, expression } ] ;
    def __init__(self, expressions):
        self.expressions = expressions


class Block:  # { statement };
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        visitor.visit_block(self)


class IfStatement:  # “if”, “(”, condition, “)”, “{“, block, “}“, [“else”, “{”, block, “}” ];
    def __init__(self, condition, block1, block2=None):
        self.condition = condition
        self.block1 = block1
        self.block2 = block2

    def accept(self, visitor):
        visitor.visit_if_statement(self)


class WhileStatement:  # “while”, “(“, condition, “)”, “{“, block, “}“ ;
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def accept(self, visitor):
        visitor.visit_while_statement(self)


class ReturnStatement:  # “return”, expression, “;” ;
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_return_statement(self)


class InitStatement:  # signature, [ assignmentOp, expression ], “;” ;
    def __init__(self, signature, expression=None):
        self.signature = signature
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_init_statement(self)


class AssignStatement:  # id, assignmentOp, expression, “;” ;
    def __init__(self, _id, expression):
        self.id = _id
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_assign_statement(self)


class PrintStatement:  # “print”, “(“, printable { “,”, printable }, “)”, ";" ;
    def __init__(self, printables):
        self.printables = printables

    def accept(self, visitor):
        visitor.visit_print_statement(self)


class Condition:  # andCond, { orOp, andCond } ;
    def __init__(self, and_conds):
        self.and_conds = and_conds


class AndCond:  # equalityCond, { andOp, equalityCond } ;
    def __init__(self, equality_conds):
        self.equality_conds = equality_conds


class EqualityCond:  # relationalCond, [ equalOp, relationalCond ] ;
    def __init__(self, relational_cond1, equal_op=None, relational_cond2=None):
        self.relational_cond1 = relational_cond1
        self.equal_op = equal_op
        self.relational_cond2 = relational_cond2


class RelationalCond:  # primaryCond, [ relationOp, primaryCond ];
    def __init__(self, primary_cond1, relation_op=None, primary_cond2=None):
        self.primary_cond1 = primary_cond1
        self.relation_op = relation_op
        self.primary_cond2 = primary_cond2


class PrimaryCond:  # [ unaryOp ], ( parenthCond | expression ) ;
    def __init__(self, unary_op=False, parenth_cond=None, expression=None):
        self.unary_op = unary_op
        self.parenth_cond = parenth_cond
        self.expression = expression


class ParenthCond:  # “(“, condition, “)” ;
    def __init__(self, condition):
        self.condition = condition


class Expression:  # multiplExpr, { additiveOp, multiplExpr } ;
    def __init__(self, multipl_exprs, additive_ops):
        self.multipl_exprs = multipl_exprs
        self.additive_ops = additive_ops

    def accept(self, visitor):
        visitor.visit_expression(self)


class MultiplExpr:  # primaryExpr, { multiplOp, primaryExpr } ;
    def __init__(self, primary_exprs, multipl_ops):
        self.primary_exprs = primary_exprs
        self.multipl_ops = multipl_ops


class PrimaryExpr:  # [ “-” ], [currency | getCurrency], ( number | id | parenthExpr | functionCall ),
    # [currency | getCurrency] ;
    def __init__(self, minus=False, currency1=None, get_currency1=None, number=None, _id=None, parenth_expr=None,
                 function_call=None, currency2=None, get_currency2=None):
        self.minus = minus
        self.currency1 = currency1
        self.get_currency1 = get_currency1
        self.number = number
        self.id = _id
        self.parenth_expr = parenth_expr
        self.function_call = function_call
        self.currency2 = currency2
        self.get_currency2 = get_currency2


class ParenthExpr:  # “(”, expression, “)” ;
    def __init__(self, expression):
        self.expression = expression


class GetCurrency:  # id, “.”, “getCurrency()” ;
    def __init__(self, _id):
        self.id = _id
