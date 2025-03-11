import asyncio


async def count_up():
    print("시작합니다")
    for i in range(5):
        await asyncio.sleep(1)
        print("{i + 1}")
    print("완료되었습니다")


async def main():
    await count_up()


asyncio.run(main())
