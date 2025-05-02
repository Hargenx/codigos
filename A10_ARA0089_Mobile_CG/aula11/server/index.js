const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());

// Rota de verificação
app.get('/api/check', (req, res) => {
    const code = parseInt(req.query.code) || 200; // código pode ser passado na URL

    console.log(`➡️ Retornando status: ${code}`);
    res.sendStatus(code);
});

app.listen(PORT, '172.16.0.41', () => {
    console.log(`✅ Servidor rodando em http://localhost:${PORT}`);
});
