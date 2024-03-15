# Criar os formulários do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta!")
    

class FormCriarConta(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    username = StringField("Usuário:", validators=[DataRequired()])
    senha = PasswordField("Senha:", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha:", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar.")
    
class FormFotos(FlaskForm):
    foto = FileField("Fotos", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")