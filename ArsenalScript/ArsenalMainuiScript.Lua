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

-- Function to apply hitbox changes to new players
local function applyHitboxToNewPlayers()
    local isOn = button.Text == "On"
    
    if isOn then
        local players = game:GetService("Players")
        local localPlayer = players.LocalPlayer
        local playerName = localPlayer.Name
        local newSize = math.clamp(tonumber(sizeInput.Text) or 13, 1, 25) -- Clamp size between 1 and 25
        
        players.PlayerAdded:Connect(function(player)
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
        end)
    end
end

-- Function to toggle enemy highlighting
local function toggleEnemyHighlight()
    local isHighlighting = highlightButton.Text == "Highlight Enemies"

    if isHighlighting then
        highlightButton.Text = "Unhighlight Enemies"
        highlightButton.TextColor3 = Color3.new(0, 1, 0) -- Change text color to green
        
        -- Function to highlight enemies through walls
        local function highlightEnemies()
            local players = game:GetService("Players")
            local localPlayer = players.LocalPlayer
            local playerName = localPlayer.Name

            for _, player in ipairs(players:GetPlayers()) do
                if player.Name ~= playerName then
                    local character = player.Character
                    if character then
                        local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
                        if humanoidRootPart then
                            -- Apply highlighting effect
                            local highlight = Instance.new("BoxHandleAdornment")
                            highlight.Size = humanoidRootPart.Size
                            highlight.Color3 = Color3.new(1, 0, 0) -- Red color
                            highlight.Transparency = 0.5 -- Semi-transparent
                            highlight.AlwaysOnTop = true
                            highlight.Adornee = humanoidRootPart
                            highlight.Parent = humanoidRootPart
                        end
                    end
                end
            end
        end

        -- Call function to highlight enemies
        highlightEnemies()

    else
        highlightButton.Text = "Highlight Enemies"
        highlightButton.TextColor3 = Color3.new(1, 0, 0) -- Change text color to red

        -- Function to remove highlighted enemies
        local function removeEnemyHighlight()
            local players = game:GetService("Players")
            local localPlayer = players.LocalPlayer
            local playerName = localPlayer.Name

            for _, player in ipairs(players:GetPlayers()) do
                if player.Name ~= playerName then
                    local character = player.Character
                    if character then
                        local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
                        if humanoidRootPart then
                            -- Remove all adornments (highlights)
                            for _, child in ipairs(humanoidRootPart:GetChildren()) do
                                if child:IsA("BoxHandleAdornment") then
                                    child:Destroy()
                                end
                            end
                        end
                    end
                end
            end
        end

        -- Call function to remove highlights
        removeEnemyHighlight()
    end
end

-- Toggle text when button is clicked
button.MouseButton1Click:Connect(function()
    toggleButtonText()
    -- Add any other actions you want to perform on button click here
end)

-- Toggle enemy highlighting when button is clicked
highlightButton.MouseButton1Click:Connect(function()
    toggleEnemyHighlight()
    -- Add any other actions you want to perform on button click here
end)

-- Call function to apply hitbox changes to new players when script starts
applyHitboxToNewPlayers()

-- Create a function to get players' name
local function getPlayersName()
    for _, v in pairs(game:GetChildren()) do
        if v.ClassName == "Players" then
            return v.Name
        end
    end
end

-- Variables to track dragging state
local dragging = false
local dragInput, dragStart, startPos

-- Function to update the position of the frame and button
local function updateInput(input)
    local delta = input.Position - dragStart
    scrollingFrame.Position = UDim2.new(startPos.X.Scale, startPos.X.Offset + delta.X, startPos.Y.Scale, startPos.Y.Offset + delta.Y)
end

-- Input event listeners for dragging
dragArea.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = true
        dragStart = input.Position
        startPos = scrollingFrame.Position

        input.Changed:Connect(function()
            if input.UserInputState == Enum.UserInputState.End then
                dragging = false
            end
        end)
    end
end)

dragArea.InputChanged:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseMovement then
        dragInput = input
    end
end)

game:GetService("UserInputService").InputChanged:Connect(function(input)
    if dragging and input == dragInput then
        updateInput(input)
    end
end)

-- Toggle visibility with 'P' key
game:GetService("UserInputService").InputBegan:Connect(function(input, gameProcessed)
    if not gameProcessed then -- Check that the game is not processing the input for another action
        if input.KeyCode == Enum.KeyCode.P then
            scrollingFrame.Visible = not scrollingFrame.Visible
            sizeInput.Position = UDim2.new(sizeInput.Position.X.Scale, sizeInput.Position.X.Offset, button.Position.Y.Scale, button.Position.Y.Offset) -- Align sizeInput vertically with button
        end
    end
end)
