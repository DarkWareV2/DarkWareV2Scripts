-- Create a new ScreenGui
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "ScriptGuiLoader"
screenGui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")

-- Create a new ScrollingFrame
local scrollingFrame = Instance.new("ScrollingFrame")
scrollingFrame.Size = UDim2.new(0, 455, 0, 547)
scrollingFrame.Position = UDim2.new(0.5, 0, 0.5, 0) -- Centering the frame on the screen
scrollingFrame.AnchorPoint = Vector2.new(0.5, 0.5) -- Setting the anchor point to the center
scrollingFrame.Parent = screenGui

-- Optional: Customize the ScrollingFrame (e.g., scroll bar, background color)
scrollingFrame.ScrollBarThickness = 10
scrollingFrame.BackgroundColor3 = Color3.fromRGB(255, 255, 255) -- White background

-- Create a draggable area at the top of the ScrollingFrame
local dragArea = Instance.new("Frame")
dragArea.Size = UDim2.new(1, 0, 0, 50) -- 50 pixels high
dragArea.Position = UDim2.new(0, 0, 0, 0)
dragArea.BackgroundTransparency = 1 -- Make it invisible
dragArea.Parent = scrollingFrame

-- Variables to track dragging state
local dragging = false
local dragInput, dragStart, startPos

-- Function to update the position of the frame
local function updateInput(input)
    local delta = input.Position - dragStart
    scrollingFrame.Position = UDim2.new(startPos.X.Scale, startPos.X.Offset + delta.X, startPos.Y.Scale, startPos.Y.Offset + delta.Y)
end

-- Input event listeners
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
