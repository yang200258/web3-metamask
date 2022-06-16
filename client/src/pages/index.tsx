import { useEffect, useState } from 'react';
import { request } from 'umi';
import BN from 'bn.js';
import { Button, Form, Input, Spin, Descriptions, InputNumber, message } from 'antd';
import styles from './index.less';


declare global {
  interface Window {
    ethereum: any;
  }
}

const App = () => {
  const [from, setFrom] = useState<any[]>([]);
  const [transactionResult, setTransactionResult] = useState<any>({});
  const [loadingText, setLoadingText] = useState('loading');
  const [loading, setLoading] = useState(true);
  const onFinish = async (values: any) => {
    setLoading(true);
    // await checkBanlance(values);
    const transactionHash = await sendTransaction(values);
    if (!transactionHash) return setLoading(false);
    message.success(`Got the Transaction hash:${transactionHash}`);
    setLoadingText('Getting the transaction result...');
    try {
      const res = await request('/rest/transfer', {
        method: 'POST',
        data: {
          transactionHash,
        },
        skipErrorHandler: true,
      });
      message.success('Congratulation,Transaction success!')
      setLoading(false);
      console.log(JSON.stringify(res));
      setTransactionResult(res);
    } catch(err: any) {
      message.error(err.data.msg);
    }
  };

  // const checkBanlance = async (values: any) => {
  //   const { amount } = values;
  //   setLoadingText('Getting block number');
  //   const blockNumber = await window.ethereum.request({
  //     method: 'eth_blockNumber',
  //   });
  //   console.log(typeof window.ethereum.selectedAddress)
  //   setLoadingText('Checking address balance');
  //   const balance = await window.ethereum.request({
  //     method: 'eth_getBalance',
  //     params: [{
  //       address: window.ethereum.selectedAddress.toString(16),
  //       blockNumber,
  //     }],
  //   });
  //   console.log(balance);
  // }

  const sendTransaction = async (values: any) => {
    const { amount, address } = values;
    setLoadingText('Making trade transaction...');
    const transactionParameters = {
      to: address,
      from: window.ethereum.selectedAddress,
      value: '0x' + new BN(String(+amount * 1e18), 10).toString(16),
      data: '', 
    };
    console.log(transactionParameters)
    try {
      const txHash = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });
      return txHash;
    } catch(e: any) {
      message.error(e.message);
      return '';
    }
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  useEffect(() => {
    if (window.ethereum) {
      const ethereum = window.ethereum;
      ethereum.request({ method: 'eth_requestAccounts' }).then((res: any[]) => {
        setFrom(res);
        setLoading(false);
      }).catch((err: any) => {
        alert('Whoops, something is error!' + err);
        setLoading(false);
      })
    } else {
      setLoading(false);
      alert('Please setup MetaMask as the first step!');
    }
  }, []);

  return (
    <Spin  spinning={loading} tip={loadingText}>
      {
      from.length > 0 ? (
        <div className={styles.content}>
      <Descriptions title="" bordered>
        <Descriptions.Item label="Current Account">{from.join(',')}</Descriptions.Item>
      </Descriptions>
      <Form
        style={{
          marginTop: 30,
        }}
        name="basic"
        onValuesChange={(changeVal, allVals) => {
          console.log(changeVal, allVals)
        }}
        initialValues={{
          address: '',
          amount: '0.00001',
        }}
        labelCol={{
          span: 4,
        }}
        wrapperCol={{
          span: 16,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        <Form.Item
          label="Address"
          name="address"
          rules={[
            {
              required: true,
              message: 'Please input your address!',
            },
          ]}
        >
          <Input placeholder='Recipient Address'/>
        </Form.Item>
        <Form.Item
          label="Token Amount"
          name="amount"
          rules={[
            {
              required: true,
              message: 'Please input your amount!',
            },
          ]}
        >
          <InputNumber min={0.00001} step={0.00001} />
        </Form.Item>
        <Form.Item
          wrapperCol={{
            offset: 8,
            span: 16,
          }}
        >
          <Button type="primary" htmlType="submit">
            transfer
          </Button>
        </Form.Item>
      </Form>
      {transactionResult['blockHash'] &&
        <Descriptions title="Transaction Result" bordered>
          {Object.keys(transactionResult).map(k => (
            <Descriptions.Item span={3} label={k} key={`transactionResult-k`}>{transactionResult[k]}</Descriptions.Item>
          ))}
        </Descriptions>
      }
      </div>
      ): 
      <span><b>Please install metamask first!</b></span>
      }
    </Spin>
  );
};

export default App;
