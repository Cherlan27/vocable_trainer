"use client";

import styles from "./page.module.css";
import { useRouter } from 'next/navigation';
import MyButton from './components/button';

export default function App() {
  const router = useRouter();

  function clickTraining() {
    console.log("Training started");
    router.push("/pages/cards");
  }

  function clickReview() {
    console.log("Review started");
    router.push("/pages/review");
  }

  function clickStats() {
    console.log("Statistics started");
    router.push("/pages/stats");
  }

  return (
    <>
      <div className={styles.page}>
        
        <main className={styles.main}>
          
          <h1 className={styles.title}>
            Welcome to the Vocable Trainer App!
          </h1>
          <div className={styles.buttonContainer}>
            <MyButton title="Learn new words" onClickButton={clickTraining} />
            <MyButton title="Review vocabulary" onClickButton={clickReview} />
            <MyButton title="Statistics" onClickButton={clickStats} />
          </div>
        </main>
        <footer className={styles.footer}>
        </footer>
      </div>
    </>
  );
}
