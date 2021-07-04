def reportarPromedio(dicReporte):
    return dicReporte["estudiante"] + " = " + str(dicReporte["promedio"])
def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas["nota1"]
    sumatoria += dicNotas["nota2"]
    sumatoria += dicNotas["nota3"]
    sumatoria += dicNotas["nota4"]
    promedio = round(sumatoria/4,2)
    reporteNotas = {
                    "promedio":promedio,
                    "estudiante":dicNotas["estudiante"]
                    }
    return reporteNotas
dicNotas = {
            "estudiante":"beneficiario Rodriguez",
            "nota1":3.0,
            "nota2":2.1,
            "nota3":5.0,
            "nota4":4.7
            }
print(reportarPromedio(generarReporteNotas(dicNotas)))
