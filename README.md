# Mantenimiento Receta Module

## Alcance del modulo

Modulo receta ficha tecnica. 

## Modelos 

### `temporada.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `componente.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `descripcion.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `secuencia.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `unimedida.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `depto.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `articulo.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `compmanu.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `factperdida.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `cantidad.model`
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

### `temporadas.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)

### `receta.model`
- Fields:
  - `name` (Char)
  - `decription` (Char)
  - `temporadas_id` (Char)
  - `temporada_id` (Char)
  - `componente_id` (Char)
  - `decripcion_id` (Char)
  - `secuencia_id` (Char)
  - `uni_medida_id` (Char)
  - `depto_id` (Char)
  - `articulo_id` (Char)
  - `comp_manu_id` (Char)
  - `fact_perdida_id` (Char)
  - `cantidad` (Char)
  - `c_unitario_id` (Char)
  - `c_ampliado_id` (Char)
  - (state)
  - `Funcion` (next_button)
  - `Funcion` (calcular_costo_ampliado)