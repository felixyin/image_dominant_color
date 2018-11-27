<?php

namespace tutorial\php;

error_reporting(E_ALL);

require_once __DIR__ . '/vendor/apache/thrift/lib/php/lib/Thrift/ClassLoader/ThriftClassLoader.php';
require_once __DIR__ . '/genphp/imagecolor/ImageColor.php';
require_once __DIR__ . '/genphp/imagecolor/Types.php';

use Thrift\ClassLoader\ThriftClassLoader;

$GEN_DIR = realpath(dirname(__FILE__) . '/..') . '/genphp';
$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', __DIR__ . '/vendor/apache/thrift/lib/php/lib');
$loader->registerDefinition('imagecolor', $GEN_DIR);
$loader->register();


use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;
use Thrift\Transport\TSocket;
use imagecolor\ImageColorClient;


try {
    $socket = new TSocket('localhost', 9090);
    $transport = new TBufferedTransport($socket, 1024, 1024);
    $protocol = new TBinaryProtocol($transport);
    $client = new ImageColorClient($protocol);

    $transport->open();

//     图片路径
    $imagePath = '/Users/fy/workspace/temp/image_dominant_color/thrift_client_php/1331543305664_.pic_hd.jpg';

    $color = $client->getColor($imagePath);
    print "imagePath=$imagePath\n<br/>";
    print "color=$color\n";

    $transport->close();

} catch (TException $tx) {
    print 'TException: ' . $tx->getMessage() . "\n";
}

