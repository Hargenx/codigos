# Nome fixo da rede
$networkName = "ESTACIO-VISITANTES"

# Exibe as opções de senha
Write-Host "Escolha a senha a ser aplicada para a rede $networkName :"
Write-Host "1 - Senha 2014: estacio@2014"
Write-Host "2 - Senha 2023: estacio@2023#"

# Lê a opção escolhida
$option = Read-Host "Digite 1 ou 2"

# Seleciona a senha conforme a opção
switch ($option) {
    "1" { $password = "estacio@2014" }
    "2" { $password = "estacio@2023#" }
    default {
        Write-Host "Opção inválida. Saindo..."
        exit
    }
}

# Cria o conteúdo XML com o perfil da rede
$xmlContent = @"
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>$networkName</name>
    <SSIDConfig>
        <SSID>
            <name>$networkName</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>$password</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
"@

# Salva o XML em um arquivo temporário
$tempFile = "$env:TEMP\wifi-profile.xml"
$xmlContent | Out-File -FilePath $tempFile -Encoding UTF8

# Remove o perfil existente para evitar conflitos
netsh wlan delete profile name="$networkName" | Out-Null

# Adiciona o novo perfil de rede
netsh wlan add profile filename="$tempFile" user=all

# Conecta à rede
netsh wlan connect name="$networkName"

Write-Host "Tentando conectar à rede '$networkName' com a senha selecionada..."

# Remove o arquivo temporário
Remove-Item $tempFile
