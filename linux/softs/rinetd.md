renetd: 端口转发

    转发配置rinetd.conf：
        0.0.0.0 port1 target_host1 targetport1
        0.0.0.0 port2 target_host2 targetport2


    run:  rinetd -c rinetd.conf