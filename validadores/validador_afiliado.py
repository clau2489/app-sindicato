# validador_afiliado.py

esquemaAfiliado = {
    'legajo' : { 'type' : 'string', 'minlength' : 8, 'maxlength' : 8 },
    'dni' : {'type' : 'integer' },
    'tipo_afiliado' : { 'type' : 'string', 'maxlength' : 20 },
    'cuil' : { 'type' : 'integer', 'max' : 99999999999 },
    'apellido' : { 'type' : 'string', 'maxlength' : 50 },
    'nombre' : { 'type': 'string', 'maxlength' : 50 },
    'fecha_nacimiento' : { 'type': 'date'},
    'edad' : { 'type': 'integer', 'max' : 130 },
    'estado_civil' : { 'type': 'string', 'maxlength' : 20 },
    'nacionalidad' : { 'type': 'string', 'maxlength' : 20 },
    'calle' : { 'type': 'string', 'maxlength' : 80 },
    'altura' : { 'type': 'integer', 'max' : 99999999 },
    'piso' : { 'type': 'string', 'maxlength' : 10 },
    'depto' : { 'type': 'string', 'maxlength' : 4 },
    'cod_postal' : { 'type': 'string', 'maxlength' : 4 },
    'barrio' : { 'type': 'string', 'maxlength' : 30 },
    'localidad' : { 'type': 'string', 'maxlength' : 50 },
    'telefono_particular' : { 'type': 'string', 'maxlength' : 20 },
    'telefono_laboral' : { 'type': 'string', 'maxlength' : 20 },
    'celular' : { 'type': 'string', 'maxlength' : 20 },
    'email' : { 'type': 'string', 'maxlength' : 80 },
    'lugar_trabajo' : { 'type': 'string', 'maxlength' : 40 },
    'jerarquia' : { 'type': 'string', 'maxlength' : 40 },
    'fecha_ingreso' : { 'type': 'date' },
    'antiguedad' : { 'type': 'integer', 'max' : 99 },
    'nivel_estudios' : { 'type': 'string', 'maxlength' : 40 },
    'cbu' : { 'type': 'string', 'maxlength' : 22 },
    'banco' : { 'type' : 'integer', 'max' : 99999999 },
    'sucursal' : { 'type' : 'string', 'maxlength' : 32}

}
