class PuestoTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.sueldo = sueldo

    def __str__(self):
        return f"Codigo: {self.codigo}, Descripción: {self.descripcion}, Área: {self.areaSolicitante}, Sueldo: {self.sueldo}"


puestos = []


# 1 - AgregaPuesto
def AgregaPuesto(codigo, descripcion, areaSolicitante, sueldo):
    for p in puestos:
        if (p.codigo == codigo or p.descripcion == descripcion or p.areaSolicitante == areaSolicitante):
            print("Error: Ya existe un puesto con ese código, descripción o área.")
            return
    puestos.append(PuestoTrabajo(codigo, descripcion, areaSolicitante, sueldo))
    print("Puesto agregado correctamente.")


# 2 - MostrarTodo
def MostrarTodo():
    print("\nLista de Puestos de Trabajo:")
    for p in puestos:
        print(p)


# 3 - BorraPuesto
def BorraPuesto(codigo):
    # Ordenar por inserción
    for i in range(1, len(puestos)):
        key = puestos[i]
        j = i - 1
        while j >= 0 and puestos[j].codigo > key.codigo:
            puestos[j + 1] = puestos[j]
            j -= 1
        puestos[j + 1] = key

    # Búsqueda lineal
    for i, p in enumerate(puestos):
        if p.codigo == codigo:
            puestos.pop(i)
            print(f"Puesto con código {codigo} eliminado.")
            return
    print("No se encontró el puesto.")


# 4 - BuscaSueldo
def BuscaSueldo(sueldo):
    # Ordenar por selección descendente
    for i in range(len(puestos)):
        max_idx = i
        for j in range(i + 1, len(puestos)):
            if puestos[j].sueldo > puestos[max_idx].sueldo:
                max_idx = j
        puestos[i], puestos[max_idx] = puestos[max_idx], puestos[i]

    # Búsqueda binaria
    low, high = 0, len(puestos) - 1
    found = []
    while low <= high:
        mid = (low + high) // 2
        if puestos[mid].sueldo == sueldo:
            # Buscar vecinos con mismo sueldo
            i = mid
            while i >= 0 and puestos[i].sueldo == sueldo:
                found.append(puestos[i])
                i -= 1
            i = mid + 1
            while i < len(puestos) and puestos[i].sueldo == sueldo:
                found.append(puestos[i])
                i += 1
            break
        elif puestos[mid].sueldo < sueldo:
            high = mid - 1
        else:
            low = mid + 1

    if found:
        print("\nPuestos encontrados con sueldo", sueldo)
        for p in found:
            print(p)
    else:
        print("No se encontraron puestos con ese sueldo.")


# 5 - ListaMasValiosa
def ListaMasValiosa(monto):
    # Ordenar por burbuja según sueldo
    n = len(puestos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puestos[j].sueldo > puestos[j + 1].sueldo:
                puestos[j], puestos[j + 1] = puestos[j + 1], puestos[j]

    seleccionados = []
    total = 0
    for p in puestos:
        if total + p.sueldo <= monto:
            seleccionados.append(p)
            total += p.sueldo

    print(f"\n Con un presupuesto de {monto}, se pueden contratar:")
    for p in seleccionados:
        print(p)
    print("Total invertido:", total)


# -------------------------------
# DEMOSTRACIÓN CON 6 PUESTOS
# -------------------------------

AgregaPuesto(101, "Analista de Datos", "TI", 3500)
AgregaPuesto(102, "Diseñador Gráfico", "Marketing", 2800)
AgregaPuesto(103, "Contador", "Finanzas", 4000)
AgregaPuesto(104, "Ingeniero de Software", "TI", 5000)
AgregaPuesto(105, "Asistente Administrativo", "Administración", 2500)
AgregaPuesto(106, "Gerente de Ventas", "Comercial", 6000)

MostrarTodo()

BorraPuesto(103)
MostrarTodo()

BuscaSueldo(2800)

ListaMasValiosa(10000)
