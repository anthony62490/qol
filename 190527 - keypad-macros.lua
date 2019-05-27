-- assign logical name to macro keyboard
lmc_assign_keyboard('MACROS');

-- define callback for whole device
lmc_set_handler('MACROS',function(button, direction)
  if (direction == 1) then return end  -- ignore down
  if     (button == string.byte('1')) then lmc_send_keys('^C')
  elseif (button == string.byte('2')) then lmc_send_keys('^V')
  elseif (button == string.byte('3')) then lmc_send_keys('^x')
  else print('Not yet assigned: ' .. button) 
  end
end)
