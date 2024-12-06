<?php

namespace App\Commands;

use CodeIgniter\CLI\BaseCommand;
use CodeIgniter\CLI\CLI;

class Websocket extends BaseCommand
{
    protected $group = 'WebSocket';
    protected $name = 'websocket:start';
    protected $description = '啟動 WebSocket 伺服器';

    public function run(array $params)
    {
        $command = 'C:/Users/96285/anaconda3/envs/ml/python.exe ' . FCPATH . 'python/ccc_website.py';  // 指向 Python 腳本
        $output = shell_exec($command);

        CLI::write("WebSocket 伺服器啟動: " . $output, 'green');

    }
}