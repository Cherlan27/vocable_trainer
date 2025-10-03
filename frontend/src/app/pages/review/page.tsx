"use client";

import Card from "@/app/components/card";
import MyButton from "@/app/components/button";
import styles from "../../page.module.css";
import { useRouter } from 'next/navigation';

export default function Review() {
  const router = useRouter();

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className="container">
          <h1>Cards Page</h1>
          <p>Lerne neue Vokables ganz easy!</p>
          <Card word="Test French" />
          <div style={{ height: '20px' }}>
            <MyButton title="Next" onClickButton={() => console.log('New Card clicked')} />
          </div>
        </div>
          <MyButton title="Back to Home" onClickButton={() => router.push('/')} />
      </main>
    </div>
  );
}