function Set-Brightness {
    param (
        [int]$level
    )
    $wmi = Get-WmiObject -Namespace root/wmi -Class WmiMonitorBrightnessMethods
    if ($wmi) {
        foreach ($monitor in $wmi) {
            $monitor.WmiSetBrightness(0, $level)
            Write-Host "Brightness set to $level%"
        }
    } else {
        Write-Host "No WMI brightness support found."
    }
}

function Get-CurrentBrightness {
    $brightnessInfo = Get-WmiObject -Namespace root/wmi -Class WmiMonitorBrightness
    if ($brightnessInfo) {
        return $brightnessInfo.CurrentBrightness
    } else {
        Write-Host "Unable to retrieve current brightness."
        return -1
    }
}

$inputString = "111110010100110100101"  # Example input string

while ($true) {
    foreach ($char in [char[]]$inputString) {
        $currentBrightness = Get-CurrentBrightness
        if ($currentBrightness -gt 96) {
            Set-Brightness -level 96
        }
        if ($currentBrightness -lt 0) {
            Set-Brightness -level 0
        }
        $currentBrightness = Get-CurrentBrightness
        
        if ($currentBrightness -eq -1) {
            Write-Host "Exiting due to error in retrieving brightness."
            break
        }
        
        if ($char -eq '1') {
            $currentBrightness += 4
            Set-Brightness -level $currentBrightness
            Start-Sleep -Milliseconds 250
            $currentBrightness -= 4
            Set-Brightness -level $currentBrightness
            Start-Sleep -Milliseconds 250
        } else {
            Set-Brightness -level $currentBrightness
            Start-Sleep -Milliseconds 250
            $currentBrightness += 4
            Set-Brightness -level $currentBrightness + 4
            Start-Sleep -Milliseconds 250
            $currentBrightness -= 4
        }
    }
}