"use client";

import styles from "./page.module.css";
import { useRouter } from 'next/navigation';
import { MyButton } from './components/button';

export default function App() {
  const router = useRouter();

  function clickManualAdd() {
    console.log("Add manual vocs to database")
    router.push("/manual")
  }

  function clickTopicAdd() {
    console.log("Add vocs due to topic based");
    router.push("/topic");
  }

  function clickReview() {
    console.log("Review started");
    router.push("/review");
  }

  return (
    <>
      <div className={styles.page}>
        <main className={styles.main}>

          <h1 className={styles.title}>
            Welcome to the Vocable Trainer App!
          </h1>
          <div className={styles.buttonContainer}>
            <MyButton title="Add new vocabulary" onClickButton={clickManualAdd} />
            <MyButton title="Learn new vocabulary based on topic" onClickButton={clickTopicAdd} />
            <MyButton title="Review your vocabulary" onClickButton={clickReview} />
            <MyButton title="Vocabulary statistics" onClickButton={() => console.log('Statistics clicked')} />
          </div>
        </main>
        <footer className={styles.footer}>
        </footer>
      </div>
    </>
  );
}
