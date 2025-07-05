# DevOps Microservice – Banco Pichincha Assessment

Este proyecto es una solución al assessment técnico DevOps para Banco Pichincha. Consiste en un microservicio REST desarrollado en Python, contenedorizado con Docker, desplegable con Kubernetes, e integrado con CI/CD usando GitHub Actions.

Daniela Estupiñan

---

## 🚀 Endpoint

- **Ruta:** `/DevOps`
- **Método:** `POST`
- **Autenticación:** API Key y JWT (en headers)
- **Content-Type:** `application/json`

### Ejemplo de request (cURL)

```bash
curl -X POST \
  -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
  -H "X-JWT-KWY: <TU_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}' \
  https://<HOST>/DevOps
