import { Table } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import shop_1 from '../storage/220997827.json';
import shop_2 from '../storage/223946658.json';


const columns: ColumnsType<any> = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
    /* render: (text) => <a>{text}</a>, */
  },
  {
    title: 'Price',
    dataIndex: 'price',
    key: 'price',
  },
]

function Pets() {
  return (
    <div className="container mx-auto px-4 p-5">
      <h1>Shop 1</h1>
      <Table columns={columns} dataSource={shop_1} />
      <h1>Shop 2</h1>
      <Table columns={columns} dataSource={shop_2} />
    </div>
  );
}

export default Pets;
