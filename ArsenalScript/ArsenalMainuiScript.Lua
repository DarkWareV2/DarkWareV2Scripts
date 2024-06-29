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
button.Text = "Button"
button.BackgroundTransparency = 1 -- Make button background fully transparent
button.TextScaled = true -- Allow text to scale with button size
button.Parent = scrollingFrame

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
local UserInputService = game:GetService("UserInputService")

UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if not gameProcessed then -- Check that the game is not processing the input for another action
        if input.KeyCode == Enum.KeyCode.P then
            scrollingFrame.Visible = not scrollingFrame.Visible
        end
    end
end)
