# Modulo Mantenimiento ficha Tecnica.

## Alcance del modulo

Modulo receta ficha tecnica. 

## Modelos 

### `temporadas.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `articulo.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)
  - `_rec_name` (nombre)
  - `nombre` (Char)

### `codigosec.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)
  - `_rec_name` (codigo)
  - `codigo` (Char)

### `componente.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)
  - `_rec_name` (codigo)
  - `codigo` (Char)
  - `descripcion` (Text)
  - `um` (Char)

### `componente.descripcion.model`
- Fields:
  - `descripcion` (Text)

### `componente.um.model`
- Fields:
  - `um` (Char)

### `compmanu.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `cantidad.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `factperdida.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `cunitario.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `campliado.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `depto.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)
_________________________________________________

### `Vista Formulario`
### `receta.model`
- Fields:
  - `temporadas_id` (Char)
  - `articulo_id` (Integer)

_________________________________________________

### `Vista Lista`
### `receta.model`
- Fields:
  - `codigosec_id` (Integer)
  - `componente_id` (Char)
  - `descripcion` (Text)
  - `comp_manu` (Char)
  - `cantidad_id` (Integer)
  - `fact_perdida_id` (Integer)
  - `c_unitario_id` (Float)
  - `c_ampliado_id` (Float)
  - `depto_id` (Char)

_________________________________________________

### `Funciones`

  - (state)
  - `Funcion` (next_button)
  - `Funcion` (calcular_costo_ampliado)
  - `Funcion` (_onchange_componente_id)
  - `Funcion` (_check_nombre)
  - `Funcion` (name_get)
  - `Funcion` (_compute_nombre_receta)
