-- Function to get the name of the Players service
local function getPlayersName()
    for _, v in pairs(game:GetChildren()) do
        if v.ClassName == "Players" then
            return v.Name
        end
    end
end

-- Create a new ScreenGui
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "ScriptGuiLoader"
screenGui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")

-- Create a new ScrollingFrame
local scrollingFrame = Instance.new("ScrollingFrame")
scrollingFrame.Size = UDim2.new(0, 455, 0, 547)
scrollingFrame.Position = UDim2.new(0.5, 0, 0.5, 0) -- Centering the frame on the screen
scrollingFrame.AnchorPoint = Vector2.new(0.5, 0.5) -- Setting the anchor point to the center
scrollingFrame.BackgroundColor3 = Color3.new(0, 0, 0) -- Black background
scrollingFrame.BorderSizePixel = 0 -- No border
scrollingFrame.Parent = screenGui

-- Create a draggable area at the top of the ScrollingFrame
local dragArea = Instance.new("Frame")
dragArea.Size = UDim2.new(1, 0, 0, 50) -- 50 pixels high
dragArea.Position = UDim2.new(0, 0, 0, 0)
dragArea.BackgroundTransparency = 1 -- Make it invisible
dragArea.Parent = scrollingFrame

-- Create a button on top of the ScrollingFrame
local button = Instance.new("TextButton")
button.Size = UDim2.new(0, 200, 0, 50) -- Button size
button.Position = UDim2.new(0.04, 0, 0.043, 0) -- Button position relative to scrollingFrame
button.Text = "Off" -- Initial text
button.BackgroundTransparency = 1 -- Make button background fully transparent
button.TextColor3 = Color3.new(1, 0, 0) -- Initial text color (red)
button.TextScaled = true -- Allow text to scale with button size
button.Parent = scrollingFrame

-- Create an input box for hitbox size
local sizeInput = Instance.new("TextBox")
sizeInput.Size = UDim2.new(0, 200, 0, 50) -- Input box size
sizeInput.Position = UDim2.new(0.618, 0, 0.043, 0) -- Position aligned vertically with the button
sizeInput.Text = "13" -- Default size value
sizeInput.BackgroundTransparency = 1 -- Make background fully transparent
sizeInput.TextColor3 = button.TextColor3 -- Match text color with button
sizeInput.TextScaled = true -- Allow text to scale with input box size
sizeInput.Parent = scrollingFrame

-- Create a highlight button
local highlightButton = Instance.new("TextButton")
highlightButton.Size = UDim2.new(0, 200, 0, 50) -- Button size
highlightButton.Position = UDim2.new(0.04, 0, 0.116, 0) -- Position below the 'Off' button
highlightButton.Text = "Highlight Enemies" -- Initial text
highlightButton.BackgroundTransparency = 1 -- Make button background fully transparent
highlightButton.TextColor3 = Color3.new(1, 0, 0) -- Initial text color (red)
highlightButton.TextScaled = true -- Allow text to scale with button size
highlightButton.Parent = scrollingFrame

-- Create a ScreenGui to hold our UI elements
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "EnemyHighlighterGui"
screenGui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")

-- Function to create UI for each enemy
local function createEnemyUI(enemy)
    local head = enemy:WaitForChild("Head")
    if not head then return end
    
    -- Create BillboardGui
    local billboardGui = Instance.new("BillboardGui")
    billboardGui.Name = "EnemyHighlighter"
    billboardGui.Size = UDim2.new(2, 0, 2, 0) -- Size of the BillboardGui
    billboardGui.AlwaysOnTop = true
    billboardGui.LightInfluence = 1 -- Make the UI visible even in dark areas
    billboardGui.Parent = head
    
    -- Create Frame inside BillboardGui
    local frame = Instance.new("Frame")
    frame.Size = UDim2.new(1, 0, 1, 0)
    frame.BackgroundTransparency = 0.5 -- Adjust transparency as needed
    frame.BackgroundColor3 = Color3.new(1, 0, 0) -- Red color
    frame.Parent = billboardGui
end

-- Function to handle enemies
local function handleEnemies()
    local players = game:GetService("Players")
    local localPlayer = players.LocalPlayer
    local playerName = localPlayer.Name
    
    -- Listen for new players being added
    players.PlayerAdded:Connect(function(player)
        if player.Name ~= playerName then
            -- Listen for their character being added
            player.CharacterAdded:Connect(function(character)
                -- Create UI for the enemy
                createEnemyUI(character)
            end)
        end
    end)
    
    -- Create UI for existing players
    for _, player in ipairs(players:GetPlayers()) do
        if player.Name ~= playerName then
            local character = player.Character
            if character then
                createEnemyUI(character)
            end
        end
    end
end

-- Start handling enemies
handleEnemies()

-- Remove UI when enemy leaves
game.Players.PlayerRemoving:Connect(function(player)
    local screenGui = screenGui:FindFirstChild("EnemyHighlighterGui")
    if screenGui then
        local billboardGui = screenGui:FindFirstChild(player.Name)
        if billboardGui then
            billboardGui:Destroy()
        end
    end
end)

-- Function to toggle the button text and adjust hitbox visibility
local function toggleButtonText()
    local isOn = button.Text == "On"
    
    if isOn then
        button.Text = "Off"
        button.TextColor3 = Color3.new(1, 0, 0) -- Change text color to red
        
        -- Show hitboxes of all players
        local players = game:GetService("Players")
        
        for _, player in ipairs(players:GetPlayers()) do
            local character = player.Character
            if character then
                local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
                local headHB = character:FindFirstChild("HeadHB")
                local leftUpperLeg = character:FindFirstChild("LeftUpperLeg")
                local rightUpperLeg = character:FindFirstChild("RightUpperLeg")
                
                if humanoidRootPart then
                    humanoidRootPart.Size = Vector3.new(1, 1, 1) -- Reset size
                    humanoidRootPart.Transparency = 0 -- Show hitbox
                    humanoidRootPart.CanCollide = true -- Enable collision
                end
                if headHB then
                    headHB.Size = Vector3.new(1, 1, 1) -- Reset size
                    headHB.Transparency = 0 -- Show hitbox
                    headHB.CanCollide = true -- Enable collision
                end
                if leftUpperLeg then
                    leftUpperLeg.Size = Vector3.new(1, 1, 1) -- Reset size
                    leftUpperLeg.Transparency = 0 -- Show hitbox
                    leftUpperLeg.CanCollide = true -- Enable collision
                end
                if rightUpperLeg then
                    rightUpperLeg.Size = Vector3.new(1, 1, 1) -- Reset size
                    rightUpperLeg.Transparency = 0 -- Show hitbox
                    rightUpperLeg.CanCollide = true -- Enable collision
                end
            end
        end
    else
        button.Text = "On"
        button.TextColor3 = Color3.new(0, 1, 0) -- Change text color to green
        
        -- Hide hitboxes of other players and adjust size
        local players = game:GetService("Players")
        local localPlayer = players.LocalPlayer
        local playerName = localPlayer.Name
        local newSize = math.clamp(tonumber(sizeInput.Text) or 13, 1, 25) -- Clamp size between 1 and 25
        
        for _, player in ipairs(players:GetPlayers()) do
            if player.Name ~= playerName then
                local character = player.Character
                if character then
                    local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
                    local headHB = character:FindFirstChild("HeadHB")
                    local leftUpperLeg = character:FindFirstChild("LeftUpperLeg")
                    local rightUpperLeg = character:FindFirstChild("RightUpperLeg")
                    
                    if humanoidRootPart then
                        humanoidRootPart.Size = Vector3.new(newSize, newSize, newSize)
                        humanoidRootPart.Transparency = 1 -- Hide if on
                        humanoidRootPart.CanCollide = false -- Disable collision if on
                    end
                    if headHB then
                        headHB.Size = Vector3.new(newSize, newSize, newSize)
                        headHB.Transparency = 1 -- Hide if on
                        headHB.CanCollide = false -- Disable collision if on
                    end
                    if leftUpperLeg then
                        leftUpperLeg.Size = Vector3.new(newSize, newSize, newSize)
                        leftUpperLeg.Transparency = 1 -- Hide if on
                        leftUpperLeg.CanCollide = false -- Disable collision if on
                    end
                    if rightUpperLeg then
                        rightUpperLeg.Size = Vector3.new(newSize, newSize, newSize)
                        rightUpperLeg.Transparency = 1 -- Hide if on
                        rightUpperLeg.CanCollide = false -- Disable collision if on
                    end
                end
            end
        end
    end
end

-- Toggle button functionality
button.MouseButton1Click:Connect(toggleButtonText)

-- Highlight button functionality
highlightButton.MouseButton1Click:Connect(function()
    local isHighlighted = highlightButton.Text == "Highlight Enemies"
    
    if isHighlighted then
        highlightButton.Text = "Highlighted"
        highlightButton.TextColor3 = Color3.new(0, 1, 0) -- Change text color to green
        
        -- Create UI for enemies
        handleEnemies()
    else
        highlightButton.Text = "Highlight Enemies"
        highlightButton.TextColor3 = Color3.new(1, 0, 0) -- Change text color to red
        
        -- Remove UI for enemies
        local screenGui = screenGui:FindFirstChild("EnemyHighlighterGui")
        if screenGui then
            for _, enemy in ipairs(screenGui:GetChildren()) do
                if enemy:IsA("BillboardGui") then
                    enemy:Destroy()
                end
            end
        end
    end
end)
