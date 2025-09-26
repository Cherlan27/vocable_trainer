"use client";

import MyButton from "@/app/components/button";
import styles from "../../page.module.css";
import { useRouter } from 'next/navigation';

export default function Cards() {
  const router = useRouter();

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div style=
          {{ 
            display: 'flex',
            flexDirection: 'column',
            height: '100px',
            justifyContent: 'center',
            alignItems: 'center',
          }}>
          <h1>Cards Page</h1>
          <p>Lerne neue Vokabeln ganz easy!</p>
        </div>
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          marginTop: '20px',
          width: '1000px',
        }}>
          <MyButton title="Back to Home" onClickButton={() => router.push('/')} />
        </div>
      </main>
    </div>
  );
}