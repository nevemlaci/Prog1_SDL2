function(copy_depend_dlls target_name)
    if(WIN32)
        add_custom_command(TARGET ${target_name} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy -t $<TARGET_FILE_DIR:${target_name}> $<TARGET_RUNTIME_DLLS:${target_name}>
                COMMAND_EXPAND_LISTS
        )
    endif (WIN32)
endfunction()